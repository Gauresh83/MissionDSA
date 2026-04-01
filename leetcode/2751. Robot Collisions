class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])
        dead = [False] * n
        st = []

        for i in order:
            if directions[i] == 'R':
                st.append(i)
            else:
                while st and directions[st[-1]] == 'R':
                    top = st[-1]
                    if healths[top] > healths[i]:
                        healths[top] -= 1
                        dead[i] = True
                        break
                    elif healths[top] < healths[i]:
                        healths[i] -= 1
                        dead[top] = True
                        st.pop()
                    else:
                        dead[i] = dead[top] = True
                        st.pop()
                        break
                if not dead[i]:
                    st.append(i)

        return [healths[i] for i in range(n) if not dead[i]]
