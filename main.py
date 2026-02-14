from reader import reader_cam_ # Function to read the camera file
from ping import ping_host  # Function to check online/offline status
from report import report_cam # Function to generate/update report

def main():
    """
        Main script responsible for:
        1. Clearing the previous report.
        2. Reading cameras from the txt file.
        3. Checking each camera's status via ping/TCP.
        4. Printing the results to the report file.
    """

    open("report.txt", "w").close() # Clear old report

    cams = reader_cam_()  # Load cameras

    for cam in cams: 
        name, model, ip = cam

      
        status = ping_host(ip)    # Check online/offline status

        print(f"{name} - {ip} - {status}")

        report_cam(name, model, status, ip) # Update report


if __name__ == "__main__":
    main()


