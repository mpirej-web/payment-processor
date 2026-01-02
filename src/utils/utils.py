import logging
import datetime
from typing import Dict, List

logger = logging.getLogger(__name__)

def validate_payment_details(payment_details: Dict) -> bool:
    required_fields = ['amount', 'currency', 'payment_method']
    for field in required_fields:
        if field not in payment_details:
            logger.error(f"Missing required field: {field}")
            return False
    return True

def calculate_payment_fee(payment_details: Dict) -> float:
    # assume fee is 2% of payment amount
    fee_percentage = 0.02
    payment_amount = payment_details['amount']
    fee = payment_amount * fee_percentage
    return fee

def generate_payment_id() -> str:
    return f"PAY-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

def process_payment(payment_details: Dict) -> Dict:
    if not validate_payment_details(payment_details):
        raise ValueError("Invalid payment details")
    payment_id = generate_payment_id()
    fee = calculate_payment_fee(payment_details)
    payment_details['payment_id'] = payment_id
    payment_details['fee'] = fee
    return payment_details

def get_payment_history(payment_ids: List[str]) -> List[Dict]:
    # simulate payment history data
    payment_history = [
        {'payment_id': 'PAY-20230220100000', 'amount': 100.0, 'currency': 'USD', 'payment_method': 'credit_card'},
        {'payment_id': 'PAY-20230220100001', 'amount': 200.0, 'currency': 'EUR', 'payment_method': 'bank_transfer'},
    ]
    return [payment for payment in payment_history if payment['payment_id'] in payment_ids]