#define bond behavior

class YieldCurve(object):

    def __init__(self):
        self.zero_rates = {}
        self.entries = {}

    def add_entry(self, par, T, coup, price, freq):
        self.entries[T] = (par, coup, price, freq)

    def get_zero_rates(self):
        self.__zero_coupons__()
        self.__get_bond_spot_rates__()
        return [self.zero_rates[T] for T in self.get_maturities()]

    def get_maturities(self):
        return sorted(self.entries.keys())

    def __zero_coupons__(self):
        for T in self.entries.keys():
            (par, coup, price, freq) = self.entries[T]
            if coup == 0:
                self.zero_rates[T] = self.zero_coupon_spot_rate(par, price, T)

    def __get_bond_spot_rates__(self):
        for T in self.get_maturities():
            entry = self.entries[T]
            (par, coup, price, freq) = entry

            if coup != 0:
                self.zero_rates[T] = self.__calculate_bond_spot_rate__(T, entry)

    def __calculate_bond_spot_rate__(self, T, entry):
        try:
            (par, coup, price, freq) = entry
            periods = T * freq
            value = price
            per_coupon = coup / freq

            for i in range(int(periods)-1):
                t = (i+1)/float(freq)
                spot_rate = self.zero_rates[t]
                discounted_coupon = per_coupon * np.exp(-spot_rate*t)
                value -= discounted_coupon

            last_period = int(periods)/float(freq)
            spot_rate = -np.log(value/(par+per_coupon))/last_period

            return spot_rate
        except:
            print("error")

    def zero_coupon_spot_rate(self, par, price, T):
        spot_rate = np.log(par/price)/T
        return spot_rate

#plot

bond_plot = YieldCurve()
bond_plot.add_entry(100, 1/12, 0., 99.80, 2)
bond_plot.add_entry(100, 2/12, 0., 99.60, 2)
bond_plot.add_entry(100, 3/12, 0., 99.4, 2)
bond_plot.add_entry(100, 6/12, 3, 100.27, 2)
bond_plot.add_entry(100, 12/12, 4, 101.57, 2)

y = bond_plot.get_zero_rates()
x = bond_plot.get_maturities()

plt.plot(x, y)
plt.title("Zero Curve")
plt.ylabel("Zero Rate")
plt.xlabel("Maturity in Years")
plt.show()
