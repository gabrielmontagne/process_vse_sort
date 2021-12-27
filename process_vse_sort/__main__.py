from xyy import process_frame, start_server, label
from pprint import pformat


@process_frame
def sort_pixels(pixs, config):
    pixs.sort(axis=0)
    print(pformat(config))
    label(
        pixs,
        str(config.get("xyy_uno", ""))
    )
    return pixs


def main():
    print('Starting process_vse_sort server')
    start_server()


if __name__ == '__main__':
    main()
