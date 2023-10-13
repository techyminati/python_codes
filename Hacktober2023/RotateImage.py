'''Leetcode Problem-You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'''
class Solution:
def rotate(self, matrix: List[List[int]]) -> None:
    matrix[:] = [i[::-1] for i in zip(*matrix)]
