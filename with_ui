import sympy as sp
import easygui as eg

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
    
    while 66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666:
        try:
            # 用户输入方程个数
            n = int(eg.enterbox("说说你有几个方程吧~（请输入数字）", "方程个数"))
            equations_input = []
            
            # 收集用户输入的方程
            for i in range(n):
                eq = eg.enterbox(f"请输入第 {i + 1} 个方程(例如: x**2 + y**2 = 1，ps：3x请写成3*x，2的2次方请写成2**2）: ","方程输入")
                if str(eq) == "None":
                    inpt = eg.buttonbox("确定要退出吗？", "退出确认", ["确定", "取消"])
                    if inpt == "确定":
                        break
                    else:
                        continue
                else:
                    equations_input.append(eq)
                
            # 求解混合类型方程组
            solutions = solve_mixed_system(equations_input)
                
            # 输出方程组的解
            # 对每个方程进行分类并准备输出类型信息
            eq_types_info = []
            for i, eq in enumerate(equations_input):
                eq_type, _ = classify_equation(eq)
                if eq_type:
                    eq_types_info.append(f"方程 {i + 1} 类型: {eq_type}")

            eq_types_str = "\n".join(eq_types_info)

            # 准备输出解的信息
            solutions_info = []
            if isinstance(solutions, list):
                for sol in solutions:
                    if isinstance(sol, dict):
                        solutions_info.append(", ".join(f"{var} = {sol[var]}" for var in sol))
                    else:
                        solutions_info.append(sol)
            elif isinstance(solutions, dict):
                solutions_info.append(", ".join(f"{var} = {sol}" for var, sol in solutions.items()))

            solutions_str = "\n".join(solutions_info)

            # 使用msgbox一次性显示所有信息
            eg.msgbox(f"方程类型:\n{eq_types_str}\n\n方程组的解:\n{solutions_str}")
        except ValueError as ve:
            eg.exceptionbox("有错误发生了，如果输入正确，请联系我们😊😊😊（ps:别忘了发错误报告，可以QQ或者github）")
        except Exception as e:
            if str(e) == "int() argument must be a string, a bytes-like object or a real number, not 'NoneType'":
                inpt = eg.buttonbox("确定要退出吗？", "退出确认", ["确定", "取消"])
                if inpt == "确定":
                    break
                else:
                    continue
            else:
                eg.exceptionbox("有错误发生了，如果输入正确，请联系我们😊😊😊（ps:别忘了发错误报告，可以QQ或者github）")

if __name__ == "__main__":
    main()
