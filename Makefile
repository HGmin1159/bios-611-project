.PHONY: clean 

clean:
	rm -rf figure
	rm -rf derived_data
	rm -rf table
	rm -f .created-dirs

.created-dirs:
	mkdir figure
	mkdir derived_data
	mkdir table
	touch .created-dirs

derived_data/contrywise_economicdata.csv: .created-dirs python/refine_economy_data.py data/WEO_Data.csv data/country_wise_latest.csv
	python3 python/refine_economy_data.py

figure/Death_Recoverd_record_contrywise.png:python/draw_figure_contry.py data/country_wise_latest.csv
	python3 python/draw_figure_contry.py

figure/Covid_Daily_Report.png: python/draw_figure_day.py data/day_wise.csv
	python3 python/draw_figure_day.py

figure/clusterandumap.png:r/analysisdr.R data/contrywise_economicdata.csv
	r r/analysisdr.R

table/result_lm.csv:r/analysislm.R data/contrywise_economicdata.csv
	r r/analysislm.R

report.pdf: derived_data/contrywise_economicdata.csv figure/Death_Recoverd_record_contrywise.png figure/Covid_Daliy_Report.png figure/clusterandumap.png table/result_lm.csv
	R -e "rmarkdown::render(\"report.Rmd\", output_format=\"pdf_document\")"