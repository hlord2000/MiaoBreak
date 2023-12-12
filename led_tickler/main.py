import serial
import time

def send_command(port, baudrate, command, wait_time=0.25):
    """
    Sends a command to the serial device and waits for a response.

    :param port: Serial port to use (e.g., '/dev/ttyACM2')
    :param baudrate: Baud rate for the serial communication
    :param command: Command string to send
    :param wait_time: Time to wait for the response (in seconds)
    :return: The response from the device
    """
    try:
        # Open the serial port
        with serial.Serial(port, baudrate, timeout=wait_time) as ser:
            # Send the command
            ser.write(command.encode())

            # Wait for the specified time to allow the device to respond
            time.sleep(wait_time)

            # Read the response
            response = ser.read(ser.inWaiting()).decode().strip()
            
            return response
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def send_led_command(port, baudrate, pin, wait_time=0.5):
    """
    Sends a LED brightness command to the serial device and waits for a response.

    :param port: Serial port to use (e.g., '/dev/ttyACM2')
    :param baudrate: Baud rate for the serial communication
    :param pin: PIN number to set the brightness for
    :param wait_time: Time to wait for the response (in seconds)
    :return: The response from the device
    """
    command = f'led set_brightness aw20216s@0 {pin} 100\r\n'
    return send_command(port, baudrate, command, wait_time)

# Example usage
port = '/dev/ttyACM2'
baudrate = 9600
recorded_pins = []

for pin in range(217):
    response = send_led_command(port, baudrate, pin)
    print(f"Response for PIN {pin}: {response}")

    user_input = input(f"Record PIN {pin}? (y/n): ").strip().lower()
    if user_input == 'y':
        recorded_pins.append(pin)

print("Recorded PINs:", recorded_pins)
