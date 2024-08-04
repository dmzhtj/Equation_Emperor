import sympy as sp

def classify_equation(equation_input):
    """
    对单个方程进行分类，判断其类型。
    :param equation_input: 用户输入的方程字符串
    :return: 方程类型和Sympy方程对象，若无法分类则返回None
    """
    try:
        # 分割方程左右两边
        left_side, right_side = equation_input.split('=')
        # 将方程左右两边转换为Sympy表达式
        left_expr = sp.sympify(left_side)
        right_expr = sp.sympify(right_side)
        # 创建Sympy方程对象
        sympy_eq = sp.Eq(left_expr, right_expr)
        
        # 判断方程是否为多项式方程及其次数
        if sympy_eq.lhs.is_polynomial():
            degree = sympy_eq.lhs.as_poly().degree()
            # 根据多项式的次数返回对应的方程类型
            return {1: "线性方程", 2: "二次方程", 3: "三次方程"}.get(degree, "高次多项式方程"), sympy_eq
        # 判断方程是否包含超越函数
        elif any(func in sympy_eq.lhs.free_symbols for func in [sp.sin, sp.cos, sp.exp, sp.log]):
            return "超越方程", sympy_eq
        
        return "其他类型方程", sympy_eq
    except Exception as e:
        print(f"在处理方程时发生错误: {e}")
        return "无法分类的方程", None

def solve_mixed_system(equations):
    """
    求解混合类型方程组。
    :param equations: 方程组列表
    :return: 方程组的解，若求解失败则返回空列表
    """
    try:
        # 定义一个空列表eqs
        eqs = []
        # 遍历equations中的每一个方程
        for eq in equations:
            # 将方程分类，得到方程的类型和方程对象
            eq_type, eq_obj = classify_equation(eq)
            # 如果方程类型存在
            if eq_type:
                # 将方程对象添加到eqs列表中
                eqs.append(eq_obj)
        # 将所有方程中的自由变量提取出来，并去重
        variables = list(set(var for eq in eqs for var in eq.free_symbols))
        # 解方程组，得到解的列表
        solutions = sp.solve(eqs, variables, dict=True)
        # 返回解的列表
        return solutions
    except Exception as e:
        print(f"在求解方程组时发生错误: {e}")
        return []

def main():
    print("____混合方程组分析与求解____")
    
    try:
        # 用户输入方程个数
        n = int(input("请输入方程的个数: "))
        equations_input = []
        
        # 收集用户输入的方程
        for i in range(n):
            eq = input(f"请输入第 {i + 1} 个方程(例如: x**2 + y**2 = 1): ")
            equations_input.append(eq)
        
        # 对每个方程进行分类并输出类型
        classifications = [classify_equation(eq) for eq in equations_input]
        for i, (eq_type, _) in enumerate(classifications):
            if eq_type:
                print(f"方程 {i + 1} 类型: {eq_type}")
        
        # 求解混合类型方程组
        solutions = solve_mixed_system(equations_input)
        
        # 输出方程组的解
        print("方程组的解为:")
        if isinstance(solutions, list):
            for sol in solutions:
                if isinstance(sol, dict):
                    print(", ".join(f"{var} = {sol[var]}" for var in sol))
                else:
                    print(sol)
        elif isinstance(solutions, dict):
            print(", ".join(f"{var} = {sol}" for var, sol in solutions.items()))
    except ValueError as ve:
        print(f"输入错误: {ve}")
    except Exception as e:
        print(f"发生了一个错误: {e}")

if __name__ == "__main__":
    main()
