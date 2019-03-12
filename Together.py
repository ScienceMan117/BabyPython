class Teams():
    """Declaring NFL variables."""
    def __init__(NFL, Winner, Loser, WinnerScore, LoserScore):
        NFL.Winner = Winner
        NFL.Loser = Loser
        NFL.WinnerScore = WinnerScore
        NFL.LoserScore = LoserScore
    
    """Print Information to the screen"""
    def Get_Message(NFL):
        Message = NFL.Winner + ' beat ' + NFL.Loser + " with a score of " + str(NFL.WinnerScore) + ' to ' + str(NFL.LoserScore)
        return Message.title()
        
