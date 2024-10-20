import laspy


def main():
	with laspy.open('data/tree 1.las') as f:
		las = f.read()
		print('Points: ', las.points)


if __name__ == "__main__":
	main()
