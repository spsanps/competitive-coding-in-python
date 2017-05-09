def minWindow(S, T):
        minWindow = [-1,-1]

        begin, end = -1, 0

        totalCount = {i:0 for i in T}

        need = {}
        for item in T:  need[item] = need.get(item, 0) + 1

        # Find the first window, containing all the characters in T
        needCount = len(T)
        while end < len(S):
            if S[end] in need:
                if begin == -1:         begin = end
                totalCount[S[end]] += 1

                if totalCount[S[end]] <= need[S[end]]:
                    # Find one more char for a qualified window
                    needCount -= 1

                    # Enough chars to form a window
                    if needCount == 0:  break
            end += 1
        else:
            # Did not find a window
            return ""

        # Try to minimize the window length by removing the leftmost items
        while True:
            if S[begin] in need:
                if totalCount[S[begin]] > need[S[begin]]:
                    totalCount[S[begin]] -= 1
                    begin += 1
                else:
                    # Already be minimum
                    break
            else:
                begin += 1

        minWindow = [begin, end]

        # Try next window, ending with S[begin]
        while True:
            # Find the next window, ending with current S[begin]
            end += 1
            while end < len(S):
                if S[end] == S[begin]:      break
                if S[end] in totalCount:    totalCount[S[end]] += 1
                end += 1
            else:
                # No windows left.
                break

            # Minimize current window, by removing the leftmost items
            begin += 1
            while begin <= end:
                if S[begin] in need:
                    if totalCount[S[begin]] > need[S[begin]]:
                        totalCount[S[begin]] -= 1
                        begin += 1
                    else:
                        # Minimized
                        break
                else:
                    begin += 1

            if end - begin < minWindow[1] - minWindow[0]:
                # Find a shorter window
                minWindow[0], minWindow[1] = begin, end

        return S[minWindow[0]: minWindow[1]+1]