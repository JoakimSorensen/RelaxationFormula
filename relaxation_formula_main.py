from relaxation import relaxation_formula

if __name__ == "__main__":
    readings = [0, 0, 0, 6, 0, 8, 0, 10, 0, 0, 3, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 1, 
            1, 0, 0]
    confidence_levels = [1, 0, 0, 0.8, 0, 0.8, 0, 0, 0, 0, 0.6, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 1, 0.8, 
            0, 0, 0, 0, 0, 0.6, 1, 0, 0]

    relaxation_formula(readings, confidence_levels)
