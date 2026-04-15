from src.checkout import *

def test_successful_purchase():
    payment = PaymentService(balance=1000)
    order = Order(total_amount=200)
    coupon = Coupon("BLACK50", 0.5)

    checkout = CheckoutService(payment)
    result = checkout.process_order(order, coupon, "BLACK50")

    assert result["status"] == "APPROVED"
