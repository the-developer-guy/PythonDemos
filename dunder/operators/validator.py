import time

class Ticket:
    """Single bus ticket. Valid for 60 minutes after use."""
    def __init__(self):
        self.timestamp = None

    def validate(self):
        if self.timestamp is None:
            self.timestamp = time.time()
    
    def is_used(self):
        return self.timestamp is not None

    def __bool__(self):
        """Check for validity.
        Valid if validated within the past 60 minutes."""
        min_valid_time = time.time() - 60*60
        if self.timestamp is None:
            return False
        
        return self.timestamp >= min_valid_time 


if __name__ == "__main__":
    new_ticket = Ticket()
    active_ticket = Ticket()
    active_ticket.validate()

    invalid_ticket = Ticket()
    invalid_ticket.timestamp = time.time() - 70*60 # used 70 minutes ago 

    print(f"New ticket is used: {new_ticket.is_used()}")
    print(f"Active ticket is used: {active_ticket.is_used()}")
    print(f"Invalid ticket is used: {invalid_ticket.is_used()}")

    # What happens here??? Try to debug!
    print(f"New ticket is valid: {new_ticket == True}")
    print(f"Active ticket is valid: {active_ticket == True}")
    print(f"Invalid ticket is valid: {invalid_ticket == True}")

    print(f"New ticket is valid: {bool(new_ticket)}")
    print(f"Active ticket is valid: {bool(active_ticket)}")
    print(f"Invalid ticket is valid: {bool(invalid_ticket)}")

