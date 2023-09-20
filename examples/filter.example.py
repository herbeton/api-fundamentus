#!/usr/bin/env python3
#
#

# import set_path_fundamentus

from fundamentus import get_resultado
from fundamentus import print_csv
from datetime import datetime, timedelta

if __name__ == '__main__':

    data = get_resultado()

    # Reorder by ticker
    data = data.sort_index(ascending=True)

    # filter on DataFrame
    data = data[ data.pl   > 0   ]
    data = data[ data.pl   < 100 ]
    data = data[ data.roe  > 0   ]
    data = data[ data.roic > 0.2   ]
    data = data[ data.c5y > 0.2   ]

    print_csv( data[ ['cotacao','pl','dy','roic','roe'] ] )

    # today's csv
    _today = datetime.today().strftime('%Y-%m-%d')
    fname = 'bovespa.detalhes.{}_new.csv'.format(_today)
    data.to_csv(fname)

