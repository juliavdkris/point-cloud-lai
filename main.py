import laspy


def main():
	with laspy.open('data/tree 1.las') as f:
		las = f.read()
		print('Points: ', las.points)
		print('Dimensions:', list(las.header.point_format.dimension_names))

		# xs = las.points.x
		# ys = las.points.y
		# zs = las.points.z
		# bbox = las.header.min, las.header.max


if __name__ == "__main__":
	main()
