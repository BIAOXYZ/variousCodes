class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        
        n = len(recipes)
        se_recipes = set(recipes)
        dic_recipes = {recipes[i]:set(ingredients[i]) for i in range(n)}
        
        def replace_complex_food(food):
            res = set()
            tmp = dic_recipes[food]
            for elem in tmp:
                if elem in se_recipes:
                    res = res | replace_complex_food(elem)
                else:
                    res.add(elem)
            dic_recipes[food] = res
            return res
        
        res = []
        se_supplies = set(supplies)
        for food in se_recipes:
            if se_supplies.issuperset(replace_complex_food(food)):
                res.append(food)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/252019143/

4 / 112 个通过测试用例
状态：执行出错


执行错误信息：
Line 15: RuntimeError: maximum recursion depth exceeded while calling a Python object
最后执行的输入：
["ju","fzjnm","x","e","zpmcz","h","q"]
[["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
["f","hveml","cpivl","d"]
"""
