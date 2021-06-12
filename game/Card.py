class Card:
    """This class is used to store a single card with a suit and a value.
    
    Suits may be:
   
    * Hearts
    * Diamonds
    * Spades 
    * Clubs

    Whereas the values may be:

    * the numbers 2-10
    * Jack
    * Queen
    * King
    * Ace

    """    
    def __init__(self, suit, value):
        """This is the constructor for the Card class

        Args:
            suit ([str): Diamonds, Hearts, Spades, or Clubs
            value ([str]): 2-10, J, Q, K, A
        """
        self.suit = suit
        self.value = value

    def change_value(self, value : str) -> None:
        """This function changes the value of a card

        Args:
            value (str): 2-10, J, Q, K, A
        """       
        self.value = value 

    def change_suit(self, suit: str) -> None:
        """Changes the suit of the card

        Args:
            suit (str): H, D, S, C
        """        
    