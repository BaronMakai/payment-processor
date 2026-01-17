import logging
from payment_processor.services import payment_service
from payment_processor.repositories import payment_repository

def main():
    logging.basicConfig(level=logging.INFO)

    try:
        payment = payment_service.process_payment(12345, 100)
        payment_repository.save_payment(payment)
        logging.info('Payment processed successfully')
    except Exception as e:
        logging.error(f'Error processing payment: {e}')

if __name__ == '__main__':
    main()