from city import City
from grepoBot import GrepoBot


def main():
    grepoBot = GrepoBot([City(17272),
			City(18388)
                         ])

    grepoBot.main()


if __name__ == "__main__":
    main()
