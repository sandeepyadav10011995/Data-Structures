class Solution:
    def restoreIpAddresses(self, string):
        path = [-1] * 4
        def snapshotIp(s, path, build_index, segment):
            # Base Case --> Our Goal
            # Catch the answers
            if segment == 4 and build_index == len(s):
                output.append(path[0] + "." + path[1] + "." + path[2] + "." + path[3])
            # Kill the overshoots
            if segment == 4 or build_index == len(s):
                return

            for i in range(1, 4):
                if i + build_index <= len(s):
                    snapshot = s[build_index: build_index + i]
                    # Our Constraints
                    if (int(snapshot) > 255) or (i >= 2 and s[build_index] == '0'):
                        break
                    # Our Choices
                    # 1. Choose
                    path[segment] = snapshot
                    # 2. Explore
                    snapshotIp(s, path, build_index + i, segment + 1)
                    # Un-choose
                    path[segment] = -1

        output = []
        snapshotIp(string, path, 0, 0)
        return output
s = '25525511135'
abc = Solution()
print(abc.restoreIpAddresses(s))
