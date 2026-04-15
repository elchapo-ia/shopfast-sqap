class PaymentException(Exception):
    pass


class InsufficientFundsException(PaymentException):
    pass


class InvalidCouponException(Exception):
    pass


class Coupon:
    def __init__(self, code: str, discount: float):
        self.code = code
        self.discount = discount

    def is_valid(self, input_code: str) -> bool:
        return self.code == input_code


class PaymentService:
    def __init__(self, balance: float):
        self.balance = balance

    def has_sufficient_balance(self, amount: float) -> bool:
        return self.balance >= amount

    def debit(self, amount: float):
        if not self.has_sufficient_balance(amount):
            raise InsufficientFundsException("Saldo insuficiente")
        self.balance -= amount


class Order:
    def __init__(self, total_amount: float):
        self.total_amount = total_amount
        self.final_amount = total_amount

    def apply_coupon(self, coupon: Coupon, input_code: str):
        if not coupon.is_valid(input_code):
            raise InvalidCouponException("Cupom inválido")

        self.final_amount = self.total_amount * (1 - coupon.discount)


class CheckoutService:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def process_order(self, order: Order, coupon: Coupon, coupon_code: str):
        
        order.apply_coupon(coupon, coupon_code)

        
        if not self.payment_service.has_sufficient_balance(order.final_amount):
            raise InsufficientFundsException("Pagamento não autorizado")

        
        self.payment_service.debit(order.final_amount)

        
        return {
            "status": "APPROVED",
            "amount_charged": order.final_amount
        }
