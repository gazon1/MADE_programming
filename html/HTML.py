from collections import deque


Debug = False
def preprocess(tag):
    return tag.replace(" ", "").lower()


YS = "CORRECT"
NO = "INCORRECT"
ALMOST = "ALMOST "


def is_tags_equal(open_tag, close_tag):
    return preprocess(open_tag)[1:-1] == preprocess(close_tag)[2:-1]


def find_closing(html_tags, close_tag):
    # returns num_erros to find closing tag in html_tags
    # and failed_tag
    if Debug:
        print("In find_closing:", html_tags, close_tag)
    if not html_tags:
        return (1, close_tag)
    else:
        last = html_tags.pop()
        if Debug:
            print("In find_closing:", html_tags)
        if is_tags_equal(last, close_tag):
            return (0, None)
        else:
            if not html_tags:
                html_tags.append(last)
                return (1, close_tag)
            else:
                pre_last = html_tags.pop()
                if Debug:
                    print("In find_closing:", html_tags)
                if is_tags_equal(pre_last, close_tag):
                    return (1, last)
                else:
                    return (2, None)


def is_closing(tag):
    return preprocess(tag)[1] == '/'


def solve(l):
    errors_num = 0
    html_tags = deque()
    failed_tag = None
    for _tag in l:
        tag = preprocess(_tag)
        if is_closing(tag):
            er, _failed_tag = find_closing(html_tags, tag)
            errors_num += er
            if Debug:
                print("after find_closing:", tag, html_tags, er, failed_tag)
                print("errors_num:", errors_num)

            if errors_num >= 2:
                return NO
            if not failed_tag:
                failed_tag = _failed_tag
        else:
            html_tags.append(tag)
    if Debug:
        print(errors_num)
    if errors_num == 0:
        if not html_tags:
            return YS
        elif len(html_tags) == 1:
            return ALMOST + html_tags.pop().upper()
        else:
            return NO
    elif errors_num == 1:
        if not html_tags:
            return ALMOST + failed_tag.upper()
        elif len(html_tags) == 1:
            return NO
            # return ALMOST + html_tags.pop().upper()
        else:
            return NO
    else:
        return NO


if __name__ == "__main__":
    x = int(input())
    for i in range(x):
        s = int(input())
        l = []
        for j in range(s):
            l.append(input())
        # print("ALMOST <HTML>")
        print(solve(l))
