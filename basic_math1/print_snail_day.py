# 2869
# 달팽이는 올라가고 싶다

snail_up, snail_slide, height = map(int, input().split())

min_day = (height - snail_up) // (snail_up - snail_slide) + 1

print(min_day)