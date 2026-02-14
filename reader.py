def reader_cam_():
    """
    Reads camera information from 'cam.txt' and returns a list of tuples.

    Each tuple contains:
        - Camera name (str)
        - Camera model (str)
        - Camera IP (str)

    Returns:
        list of tuples: [(cam_name, cam_model, cam_ip), ...]
    """
    cameras = []

    with open("cam.txt", "r") as f:
        next(f)  # Skip header line

        for line in f:
            parts = line.strip().split("|")

            # Ensure line has exactly 3 elements
            if len(parts) == 3:
                cam_name = parts[0].strip()
                cam_model = parts[1].strip()
                cam_ip = parts[2].strip()

                cameras.append((cam_name, cam_model, cam_ip))

    return cameras
