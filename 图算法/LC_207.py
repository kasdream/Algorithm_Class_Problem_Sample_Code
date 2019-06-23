class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #边界条件
        if numCourses == 1: return True
        #新建入度数组和边数组
        in_d = [0 for i in range(numCourses)]
        e = [[] for i in range(numCourses)]
        #建图，初始化入度数组
        for a,b in prerequisites:
            e[b].append(a)
            in_d[a] += 1
        #新建队列，把所有入度为0的点放入
        import Queue
        q = Queue.Queue()
        for i in range(numCourses):
            if in_d[i] == 0:
                q.put(i)
        #当队列不为空
        while not q.empty():
            x = q.get()
            #遍历队首的所有相邻节点
            for y in e[x]:
                #入度减1
                in_d[y] -= 1
                #入度为0则入队
                if in_d[y] == 0:
                    q.put(y)
        #最后判断是否有点入度不为0
        for i in range(numCourses):
            if in_d[i] != 0:
                return False
        return True
