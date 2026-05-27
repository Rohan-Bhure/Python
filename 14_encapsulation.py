# Encapsulation is wrapping methods+variable in single unit which provides 
# security and privacy. Class is a standard example of Encapsulation
# controlling direct access of data
# Features -> data hiding, prevent accendetal modification 

# public(x) (access variable anywhere),
# protected(_x) (access inside in same and sub class),
# private(__X) (access only in same class)

# Digital wallet (Fintech Code)
from __future__ import annotations

from datetime import datetime, date, timezone
from typing import Any, Dict, List


class WalletError(Exception):
    """Base exception for wallet-related errors."""


class AuthenticationError(WalletError):
    """Raised when PIN authentication fails."""


class ValidationError(WalletError):
    """Raised when input validation fails."""


class WalletLockedError(WalletError):
    """Raised when wallet is locked after too many failed attempts."""


class DigitalWallet:
    total_wallets_created = 0
    _next_transaction_id = 1
    default_daily_transfer_limit = 5

    @staticmethod
    def validate_pin(pin: str) -> bool:
        return isinstance(pin, str) and len(pin) == 4 and pin.isdigit()

    @classmethod
    def _generate_transaction_id(cls) -> int:
        tx_id = cls._next_transaction_id
        cls._next_transaction_id += 1
        return tx_id

    @classmethod
    def get_total_wallets_created(cls) -> int:
        return cls.total_wallets_created

    def __init__(
        self,
        user_name: str,
        wallet_id: str,
        initial_balance: float,
        pin: str,
        daily_transfer_limit: int = default_daily_transfer_limit,
    ) -> None:
        if not user_name or not isinstance(user_name, str):
            raise ValidationError("user_name must be a non-empty string.")

        if not wallet_id or not isinstance(wallet_id, str):
            raise ValidationError("wallet_id must be a non-empty string.")

        if initial_balance < 0:
            raise ValidationError("initial_balance cannot be negative.")

        if daily_transfer_limit <= 0:
            raise ValidationError("daily_transfer_limit must be greater than 0.")

        if not self.validate_pin(pin):
            raise ValidationError("PIN must contain exactly 4 digits.")

        self.user_name = user_name
        self.__wallet_id = wallet_id
        self.__pin = pin
        self.__current_balance = float(initial_balance)

        self.__daily_transfer_limit = daily_transfer_limit
        self.__remaining_transfers_today = daily_transfer_limit
        self.__last_transfer_reset_date = date.today()

        self.__transaction_history: List[Dict[str, Any]] = []
        self.__wrong_pin_count = 0
        self.__locked = False

        DigitalWallet.total_wallets_created += 1

    def _ensure_active(self) -> None:
        if self.__locked:
            raise WalletLockedError("Wallet is locked due to multiple wrong PIN attempts.")

    def _authenticate(self, pin: str) -> None:
        self._ensure_active()

        if pin != self.__pin:
            self.__wrong_pin_count += 1
            if self.__wrong_pin_count >= 3:
                self.__locked = True
                raise WalletLockedError("Wallet locked after 3 wrong PIN attempts.")
            raise AuthenticationError("Invalid PIN.")

        self.__wrong_pin_count = 0

    def _refresh_daily_transfer_limit_if_needed(self) -> None:
        today = date.today()
        if today != self.__last_transfer_reset_date:
            self.__remaining_transfers_today = self.__daily_transfer_limit
            self.__last_transfer_reset_date = today

    def _record_transaction(
        self,
        transaction_type: str,
        amount: float,
        balance_after: float,
        reference: str = "",
    ) -> None:
        self.__transaction_history.append(
            {
                "transaction_id": DigitalWallet._generate_transaction_id(),
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "type": transaction_type,
                "amount": round(float(amount), 2),
                "balance_after": round(float(balance_after), 2),
                "reference": reference,
            }
        )

    def _credit_transfer(self, amount: float, from_wallet_id: str) -> None:
        self.__current_balance += amount
        self._record_transaction(
            transaction_type="transfer_in",
            amount=amount,
            balance_after=self.__current_balance,
            reference=f"from:{from_wallet_id}",
        )

    def deposit(self, amount: float) -> float:
        self._ensure_active()

        if amount <= 0:
            raise ValidationError("Deposit amount must be positive.")

        self.__current_balance += amount
        self._record_transaction(
            transaction_type="deposit",
            amount=amount,
            balance_after=self.__current_balance,
        )
        return self.__current_balance

    def withdraw(self, amount: float, pin: str) -> float:
        self._authenticate(pin)

        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive.")

        if amount > self.__current_balance:
            raise ValidationError("Insufficient balance.")

        self.__current_balance -= amount
        self._record_transaction(
            transaction_type="withdraw",
            amount=amount,
            balance_after=self.__current_balance,
        )
        return self.__current_balance

    def transfer(self, other_wallet: "DigitalWallet", amount: float, pin: str) -> float:
        self._authenticate(pin)

        if not isinstance(other_wallet, DigitalWallet):
            raise ValidationError("other_wallet must be a DigitalWallet object.")

        if other_wallet is self:
            raise ValidationError("Cannot transfer to the same wallet.")

        if amount <= 0:
            raise ValidationError("Transfer amount must be positive.")

        self._refresh_daily_transfer_limit_if_needed()

        if self.__remaining_transfers_today <= 0:
            raise ValidationError("Daily transfer limit exceeded.")

        if amount > self.__current_balance:
            raise ValidationError("Insufficient balance.")

        self.__current_balance -= amount
        other_wallet._credit_transfer(amount, from_wallet_id=self.__wallet_id)

        self.__remaining_transfers_today -= 1

        self._record_transaction(
            transaction_type="transfer_out",
            amount=amount,
            balance_after=self.__current_balance,
            reference=f"to:{other_wallet.__wallet_id}",
        )

        return self.__current_balance

    def change_pin(self, old_pin: str, new_pin: str) -> None:
        self._authenticate(old_pin)

        if not self.validate_pin(new_pin):
            raise ValidationError("New PIN must contain exactly 4 digits.")

        self.__pin = new_pin
        self._record_transaction(
            transaction_type="pin_change",
            amount=0,
            balance_after=self.__current_balance,
        )

    def get_transaction_history(self, pin: str) -> List[Dict[str, Any]]:
        self._authenticate(pin)
        return [transaction.copy() for transaction in self.__transaction_history]

    def get_balance(self, pin: str) -> float:
        self._authenticate(pin)
        return round(self.__current_balance, 2)

    def get_wallet_info(self) -> Dict[str, Any]:
        return {
            "user_name": self.user_name,
            "wallet_id": self.__wallet_id,
            "locked": self.__locked,
            "remaining_transfers_today": self.__remaining_transfers_today,
            "total_transactions": len(self.__transaction_history),
        }

    def lock_wallet(self) -> None:
        self.__locked = True

    def unlock_wallet(self, pin: str) -> None:
        self._authenticate(pin)
        self.__locked = False
        self.__wrong_pin_count = 0

    def __repr__(self) -> str:
        return f"DigitalWallet(user_name={self.user_name!r}, wallet_id=****{self.__wallet_id[-4:]!r})" 
    

w1 = DigitalWallet("Rohan", "W1001", 1000, "1234", daily_transfer_limit=2)
w2 = DigitalWallet("Aman", "W1002", 500, "5678", daily_transfer_limit=2)

w1.deposit(250)
w1.withdraw(100, "1234")
w1.transfer(w2, 300, "1234")
w1.change_pin("1234", "4321")
w2.deposit(50000)
print(w1.get_balance("4321"))
print(w1.get_transaction_history("4321"))
print(DigitalWallet.get_total_wallets_created())