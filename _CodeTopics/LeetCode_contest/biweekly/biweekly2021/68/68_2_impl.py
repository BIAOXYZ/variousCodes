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
        
        def replace_complex_food(food, visiting):
            if dic_recipes[food] & se_recipes == set():
                return dic_recipes[food], True
            if food in visiting:
                return [], False
            visiting.add(food)
            res = set()
            tmp = dic_recipes[food]
            for elem in tmp:
                if elem in se_recipes:
                    dependent, flag = replace_complex_food(elem, visiting)
                    if flag:
                        res = res | dependent
                    else:
                        break
                else:
                    res.add(elem)
            if flag:
                dic_recipes[food] = res
                return res, True
            else:
                return [], False
        
        res = []
        se_supplies = set(supplies)
        for food in se_recipes:
            visiting = set()
            dependent, flag = replace_complex_food(food, visiting)
            if flag and se_supplies.issuperset(dependent):
                res.append(food)
                se_recipes.add(food)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/252030775/

112 / 112 个通过测试用例
状态：通过
执行用时: 256 ms
内存消耗: 27.1 MB
"""
