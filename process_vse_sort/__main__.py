from xyy import process_frame, start_server

@process_frame
def sort_pixels(pixs, input_path):
    print('sort pixels', pixs, input_path)

def main():
    print('running module process_vse_sort')
    start_server()

if __name__ == '__main__':
    main()
