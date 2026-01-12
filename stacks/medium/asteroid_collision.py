#link: https://neetcode.io/problems/asteroid-collision/question?list=allNC
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        check = False
        i = 0
        while True:
            if i == len(asteroids) - 1  or asteroids ==[]:
                break
            if asteroids[i] > 0 and asteroids[i+1]>0 or asteroids[i] < 0 and asteroids[i+1]<0 :
                i+=1 
            elif  abs(asteroids[i]) == abs(asteroids[i+1]) and asteroids[i] >0:
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i=0
            elif abs(asteroids[i]) > abs(asteroids[i+1]) and asteroids[i] > 0:
                asteroids.pop(i+1)
                i=0
            elif abs(asteroids[i]) < abs(asteroids[i+1]) and asteroids[i] >0 :
                    asteroids.pop(i)
                    i=0
            else:
                i+=1
        return asteroids 
