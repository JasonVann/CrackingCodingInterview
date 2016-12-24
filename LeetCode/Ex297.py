class Ex297:
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        if data == 'None':
            return None
        res = data.split(',')
        #res = data
        head = TreeNode(int(res[0]))
        head0 = head
        #if isinstance(res[0], str):
            #res[0] = [res[0]]
        #for i in range(len(res) - 1):
        queue = deque()
        queue.append(head)
        i = 0
        l = 1
        is_left = True
        #print 84, head
        none_count = 0
        #last_level_none_count = 0
        last_level = deque([])
        for r in range(1, len(res)):   
            #print 86, queue, is_left, res[r], r
                            
            if is_left:
                is_left = not is_left    
                if res[r] == 'None':
                    #queue.append('None')
                    none_count += 1
                else:
                    node1 = TreeNode(int(res[r]))
                    queue[0].left = node1
                    queue.append(node1)
            else:
                is_left = not is_left    
                
                if res[r] == 'None':
                    queue.popleft()
                    #queue.append('None')
                    none_count += 1
                else:
                    node2 = TreeNode(int(res[r]))
                    
                    queue[0].right = node2
                    queue.popleft()
                    '''
                    if none_count == 0:
                        queue.popleft()
                    else:
                        none_count -= 2
                    '''
                    queue.append(node2)
                       
        
        return head0
                
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """        
        from collections import deque
        res = ''
        if root == None:
            return 'None'
                        
        #queue = []
        queue = deque()
        queue.append([root])
        res = [str(root.val)]
        last_level = []
        last_level_none_count = 0
        while len(queue) > 0:
            level = []
            temp = queue[0]
            level0 = []
            found_real_node = False
            for node in temp:  
                #level0.append(node.val)
                if node.val == None:
                    #last_level_none_count -= 2
                    continue
                if node.left != None:
                    level.append(node.left)
                    level0.append(str(node.left.val))
                    found_real_node = True
                else:
                    null_node = TreeNode(None)
                    level.append(null_node)
                    level0.append('None')
                    last_level_none_count += 1
                if node.right != None:
                    found_real_node = True
                    level.append(node.right)
                    level0.append(str(node.right.val))
                else:
                    null_node = TreeNode(None)
                    level.append(null_node)
                    level0.append('None')
            if not found_real_node:
                break
            if level != []:
                queue.append(level)
            queue.popleft()
            #level0 = [str(a) for a in level0]
            if level0!= []:
                res.append(','.join(level0))
            last_level = list(queue)
        return ','.join(res)
    
    def serialize0(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 2**L, too slow
        res = ''
        if root == None:
            return 'None'
            
        queue = []
        queue.append([root])
        res = [str(root.val)]
        while len(queue) > 0:
            level = []
            temp = queue[0]
            level0 = []
            found_real_node = False
            for node in temp:  
                #level0.append(node.val)
                if node.left != None:
                    level.append(node.left)
                    level0.append(str(node.left.val))
                    found_real_node = True
                else:
                    null_node = TreeNode(None)
                    level.append(null_node)
                    level0.append('None')
                if node.right != None:
                    found_real_node = True
                    level.append(node.right)
                    level0.append(str(node.right.val))
                else:
                    null_node = TreeNode(None)
                    level.append(null_node)
                    level0.append('None')
            if not found_real_node:
                break
            if level != []:
                queue.append(level)
            queue.pop(0)
            #level0 = [str(a) for a in level0]
            if level0!= []:
                res.append(','.join(level0))
        return ','.join(res)

'''
public class Codec {
    private static final String spliter = ",";
    private static final String NN = "X";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        return sb.toString();
    }

    private void buildString(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append(NN).append(spliter);
        } else {
            sb.append(node.val).append(spliter);
            buildString(node.left, sb);
            buildString(node.right,sb);
        }
    }
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(spliter)));
        return buildTree(nodes);
    }
    
    private TreeNode buildTree(Deque<String> nodes) {
        String val = nodes.remove();
        if (val.equals(NN)) return null;
        else {
            TreeNode node = new TreeNode(Integer.valueOf(val));
            node.left = buildTree(nodes);
            node.right = buildTree(nodes);
            return node;
        }
    }
}
'''

class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
        
ex297 = Ex297()
#data = ["1","2","3","None","None","4","5"]
data = ['5','2','3','None','None','2','4','None','None','None','None','3','1','None','None']
print 297, ex297.deserialize(data)

