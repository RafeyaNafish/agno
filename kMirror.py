class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_k_pal(num):
            base_k = ''
            x = num
            while x > 0:
                base_k = str(x % k) + base_k
                x //= k
            return base_k == base_k[::-1]
        
        def gen_palindromes(length):
            # Generate palindromes of given length in base 10
            if length == 1:
                for i in range(1, 10):
                    yield i
                return
            half = (length + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half
            for num in range(start, end):
                s = str(num)
                if length % 2 == 0:
                    yield int(s + s[::-1])
                else:
                    yield int(s + s[-2::-1])
        
        total = 0
        count = 0
        length = 1
        
        # Keep generating palindromes until we get n of them that are k-palindromes
        while count < n:
            for num in gen_palindromes(length):
                if is_k_pal(num):
                    total += num
                    count += 1
                    if count == n:
                        return total
            length += 1
