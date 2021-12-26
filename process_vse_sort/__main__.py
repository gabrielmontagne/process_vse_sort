from xyy import process_frame, start_server


@process_frame
def sort_pixels(pixs, config):
    pixs.sort(axis=0)
    return pixs


def main():
    print('Starting process_vse_sort server')
    start_server()


if __name__ == '__main__':
    main()
