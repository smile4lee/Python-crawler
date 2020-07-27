from scihub import SciHub
import sys

title = 'Remote sensing and land cover area estimation'

sci_hub = SciHub(
    title,
)


def main():
    sci_hub.do()


if __name__ == "__main__":
    main()
    sys.exit(0)
