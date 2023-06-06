package main

import (
	"math"
)

type ExamRoom struct {
	LenOfSeat  int
	ListOfSeat []int
}

func Constructor(n int) ExamRoom {
	var a ExamRoom = ExamRoom{LenOfSeat: n,
		ListOfSeat: make([]int, 0, 0),
	}

	return a
}

func (this *ExamRoom) Seat() int {
	var selected_seat int

	if len(this.ListOfSeat) == 0 {
		this.ListOfSeat = append(this.ListOfSeat, 0)
		selected_seat = 0
	} else if len(this.ListOfSeat) == 1 {
		if this.ListOfSeat[len(this.ListOfSeat)-1] == this.LenOfSeat-1 {
			this.ListOfSeat = []int{0, this.LenOfSeat - 1}
			selected_seat = 0
		} else if this.ListOfSeat[len(this.ListOfSeat)-1] == 0 {
			this.ListOfSeat = []int{0, this.LenOfSeat - 1}
			selected_seat = this.LenOfSeat - 1
		} else {
			if this.LenOfSeat-1-this.ListOfSeat[len(this.ListOfSeat)-1] > this.ListOfSeat[len(this.ListOfSeat)-1] {
				selected_seat = this.LenOfSeat - 1
			} else {
				selected_seat = 0
			}

			if selected_seat == 0 {
				this.ListOfSeat = append([]int{selected_seat}, this.ListOfSeat...)
			} else {
				this.ListOfSeat = append(this.ListOfSeat, selected_seat)
			}
		}

	} else {
		var inserted_idx int
		var max_len int
		if this.ListOfSeat[0] == 0 {
			selected_seat = -1
			inserted_idx = -1
			max_len = math.MinInt
		} else {
			selected_seat = 0
			inserted_idx = 0
			max_len = this.ListOfSeat[0]
		}

		for idx, _ := range this.ListOfSeat {
			if idx == 0 {
				continue
			}
			if this.ListOfSeat[idx] == this.ListOfSeat[idx-1]+1 {
				continue
			}
			temp_len := (this.ListOfSeat[idx] - this.ListOfSeat[idx-1]) / 2
			if temp_len > max_len {
				selected_seat = this.ListOfSeat[idx-1] + temp_len
				max_len = temp_len
				inserted_idx = idx
			}
		}
		if this.ListOfSeat[len(this.ListOfSeat)-1] < this.LenOfSeat-1 {
			if this.LenOfSeat-1-this.ListOfSeat[len(this.ListOfSeat)-1] > max_len {
				selected_seat = this.LenOfSeat - 1
				inserted_idx = this.LenOfSeat
			}
		}
		if inserted_idx == this.LenOfSeat {
			this.ListOfSeat = append(this.ListOfSeat, selected_seat)
		} else if inserted_idx == 0 {
			this.ListOfSeat = append([]int{selected_seat}, this.ListOfSeat...)
		} else {
			this.ListOfSeat = append(this.ListOfSeat[:inserted_idx+1], this.ListOfSeat[inserted_idx:]...)
			this.ListOfSeat[inserted_idx] = selected_seat
		}
	}
	return selected_seat
}

func (this *ExamRoom) Leave(p int) {
	/*
		for idx, val := range this.ListOfSeat {
			if val == p {
				this.ListOfSeat = append(this.ListOfSeat[:idx], this.ListOfSeat[idx+1:]...)
				break
			}
		}

	*/
	dst_idx := -1
	left := 0
	right := len(this.ListOfSeat) - 1
	for left <= right {
		mid := (left + right) / 2
		if this.ListOfSeat[mid] == p {
			dst_idx = mid
			break
		} else if this.ListOfSeat[mid] > p {
			right = mid - 1
		} else {

			left = mid + 1
		}
	}
	this.ListOfSeat = append(this.ListOfSeat[:dst_idx], this.ListOfSeat[dst_idx+1:]...)

}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Seat();
 * obj.Leave(p);
 */
/*
func main() {
	obj := Constructor(10)
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	obj.Leave(0)
	obj.Leave(4)
	fmt.Println(obj.Seat())
}
*/
