package main

import "fmt"

func exist(board [][]byte, word string) bool {
	var visited [][]string = make([][]string, len(board))

	for idx, _ := range visited {
		var temp []string = make([]string, len(board[0]))
		for j, _ := range temp {
			temp[j] = "unvisited"
		}
		visited[idx] = temp
	}
	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[0]); col++ {
			if word[0] == board[row][col] {
				visited[row][col] = "visited"
				if dfs(visited, board, word, 1, row, col) {
					return true
				}
				visited[row][col] = "unvisited"
			}
		}
	}
	return false
}

var movement [][]int = [][]int{
	{1, 0},
	{-1, 0},
	{0, 1},
	{0, -1},
}

func dfs(visited [][]string, board [][]byte, word string, word_idx int, cur_row int, cur_col int) bool {
	if word_idx >= len(word) {
		return true
	}
	for _, val := range movement {
		x := cur_row + val[0]
		y := cur_col + val[1]

		if (x < 0 || x >= len(board)) || (y < 0 || y >= len(board[0])) {
			continue
		}
		if visited[x][y] == "visited" {
			continue
		}
		if word[word_idx] == board[x][y] {
			visited[x][y] = "visited"
			res := dfs(visited, board, word, word_idx+1, x, y)
			visited[x][y] = "unvisited"
			if res {
				return true
			}
		}

	}
	return false
}

func main() {
	board := [][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'F'}}
	word := "ABCB"
	fmt.Println(exist(board, word))
}
