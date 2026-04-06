
def partHelper(s, index):
    limit = len(s)
    pass_list = []

    for l in range(1, limit+1):
        print('l: ', l)
        window = s[index:index+l]

        if window == window[::-1]:
            if l+index == limit:
                pass_list.append([window])
                return pass_list
            else:
                print('before index: ', index)
                prev_list = partHelper(s, index+l)
                print('after index:', index, window)
                for i in prev_list:
                    new = [window] + i
                    print('new: ',new)
                    pass_list.append(new)
                # return pass_list
        else:
            if l+index == limit:
                return pass_list
            # else:
            #     prev_list = partHelper(s, index+l)
            #     pass_list.append(prev_list)

               
            


            
    return pass_list

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        return partHelper(s, 0)