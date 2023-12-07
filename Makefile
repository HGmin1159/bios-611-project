contrywise_economicdata.csv:python/refine_economy_data.py,data/WEO_Data.csv
	python3 python/refine_economy_data.py

Death_Recoverd_record_contrywise.png:python/draw_figure_contry.py,data/country_wise_latest.csv
	python3 python/draw_figure_contry.py

Death_Recovered_record_daywise.png:python/draw_figure_day.py,data/day_wise.csv
	python3 python/draw_figure_day.py

clusterandumap.png:r/analysisdr.R,data/contrywise_economicdata.csv
	r r/analysisdr.R

result_lm.csv:r/analysislm.R,data/contrywise_economicdata.csv
	r r/analysislm.R