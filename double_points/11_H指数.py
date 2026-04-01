def hIndex(citations: list[int]) -> int:
    sorted_citations = sorted(citations, reverse=True)
    print(sorted_citations)
    h = 0
    for i in range(len(sorted_citations)):
        if sorted_citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h


# citations = [1,3,1]
citations = [3,0,6,1,5]
print(hIndex(citations))

'''
给一个整数数组c c[i]为 第 i 篇论文被引用的次数，计算并返回该研究者的 h 指数(  1篇100次引用，100篇1次引用 h指数都是1，篇数与引用数的强关联绑定其实是)
可以先排序   
然后循环 第 i 篇的引用数 >= i + 1，满足h指数  否则不满足跳出循环

'''