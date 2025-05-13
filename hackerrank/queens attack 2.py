def queensAttack(n, k, r_q, c_q, obstacles):

    SQUARE_INF = 1


    queen_inital_pos = [r_q, c_q]
    # Updaters for movements for every queen's direction
    updaters = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    max_movements_per_quadrant = {
        (-1, -1): min(r_q - SQUARE_INF, c_q - SQUARE_INF),
        (-1, 0): r_q - SQUARE_INF,
        (-1, 1): min(r_q - SQUARE_INF, n - c_q),
        (0, -1): c_q - SQUARE_INF,
        (0, 1):  n - c_q,
        (1, -1): min(n - r_q, c_q - SQUARE_INF),
        (1, 0): n - r_q,
        (1, 1): min(n - r_q, n - c_q),
    }
    # Faster than list for searching
    obstacles_set = {(r, c) for r, c in obstacles}
      
    all_movements = 0

    for updater in updaters:
       
        for step in range(1, max_movements_per_quadrant[updater] + 1):
            
            next_coord = (
                queen_inital_pos[0] + (updater[0] * step), 
                queen_inital_pos[1] + (updater[1] * step)
            )
            
            if next_coord in obstacles_set:
                break
            
            all_movements += 1
        
    return all_movements