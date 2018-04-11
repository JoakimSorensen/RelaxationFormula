import matplotlib.pyplot as plt
from openpyxl import Workbook

def __relaxation_help_calc__(init_vals, conf_vals, prev_vals):
    result = []
    for i in range(len(init_vals)):
        j, k = i, i
        if(i == 0): 
            j = 1  
        if(i == len(init_vals) - 1): 
            k = i - 1
        result.append(conf_vals[i] * init_vals[i] 
                + (1 - conf_vals[i]) * (prev_vals[j - 1] + prev_vals[k + 1]) / 2)
    return result


def relaxation_formula(init_vals, conf_vals, loops=40, print_rate=5):
    if not len(init_vals) == len(conf_vals):
        print("The arrays need to be same size!")

    wb = Workbook()
    ws = wb.active
    ws.append(["read values"])
    ws.append(init_vals)
    ws.append(["confidence levels"])
    ws.append(conf_vals)

    prev_result = __relaxation_help_calc__(init_vals, conf_vals, init_vals)
    result = []
    ind = 0
    fig_nmr = 1
    plt.figure(fig_nmr)
    plot_cnt = 0
    for i in range(loops):
        result = __relaxation_help_calc__(init_vals, conf_vals, prev_result)
        if ind % print_rate == 0 or i == 0 or i == len(range(loops)) - 1:
            try:
                #plt.subplot(121 + plot_cnt)
                plot_cnt += 1
            except IndexError:
                plot_cnt = 0
                fig_nmr += 1
                #plt.figure(fig_nmr)
                #plt.subplot(120 + plot_cnt)
            plt.plot(result)
            plt.title("Iteration {}".format(ind))
            ws.append(["Iteration {}".format(ind)])
            ws.append(result)
        if result == prev_result:
            break
        prev_result = result
        ind += 1
    ws.append(["Iteration {}".format(ind)])
    ws.append(result)
    wb.save("relaxation_formula_ex.xlsx")
    plt.tight_layout()
    plt.show()
    print("Result = {}\nIterations = {}".format(result, ind))

