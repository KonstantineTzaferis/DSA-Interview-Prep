class Solution:
	def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
		ROWS, COLS = len(image), len(image[0])
		starting = image[sr][sc]
		visit = set()

		def dfs(grid, r, c, color):
			if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != starting or (r, c) in visit:
				return

			if grid[r][c] == starting:
				grid[r][c] = color

			visit.add((r, c))

			dfs(grid, r + 1, c, color)
			dfs(grid, r - 1, c, color)
			dfs(grid, r, c + 1, color)
			dfs(grid, r, c - 1, color)

			return grid

		dfs(image, sr, sc, color)
		return image
