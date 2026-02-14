def report_cam(cam_name, cam_model, cam_status, cam_ip):
    """
    Appends camera information and status to 'report.txt'.

    Parameters:
        cam_name (str): Name of the camera
        cam_model (str): Model/type of the camera
        cam_status (str): 'Online' or 'Offline'
        cam_ip (str): IP address of the camera
    """
    # Open the file in append mode to add data without overwriting
    with open("report.txt", "a") as f:
        f.write(f"Name: {cam_name}\n")
        f.write(f"Model: {cam_model}\n")
        f.write(f"IP: {cam_ip}\n")
        f.write(f"Status: {cam_status}\n")
        f.write("-------------\n")
