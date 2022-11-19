from golf_sim import GolfSim


if __name__ == '__main__':
    gs = GolfSim(club_face=GolfSim.FACE_CLOSED)
    #gs = GolfSim(club_face=GolfSim.FACE_OPEN)
    gs.animate()