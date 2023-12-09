.PHONY: clean 

clean:
	rm -rf figure
	rm -rf derived_data
	rm -rf table
	rm -rf report.html
	rm -rf .created-dirs

.created-dirs:
	mkdir -p figure
	mkdir -p derived_data
	mkdir -p table
	touch .created-dirs

derived_data/contrywise_economicdata.csv: .created-dirs python/refine_economy_data.py data/WEO_Data.csv data/country_wise_latest.csv
	python python/refine_economy_data.py

figure/Death_Recoverd_record_contrywise.png: .created-dirs python/draw_figure_contry.py data/country_wise_latest.csv
	python python/draw_figure_contry.py

figure/Covid_Daily_Report.png: .created-dirs python/draw_figure_day.py data/day_wise.csv
	python python/draw_figure_day.py

figure/clusterandumap.png: .created-dirs r/analysisdr.R derived_data/contrywise_economicdata.csv
	Rscript r/analysisdr.R
figure/clusterandumap2.png: .created-dirs r/analysisdr2.R derived_data/contrywise_economicdata.csv
	Rscript r/analysisdr2.R
	
table/result_lm.csv: .created-dirs r/analysislm.R derived_data/contrywise_economicdata.csv
	Rscript r/analysislm.R

report.html: .created-dirs derived_data/contrywise_economicdata.csv figure/Death_Recoverd_record_contrywise.png figure/Covid_Daily_Report.png figure/clusterandumap.png figure/clusterandumap2.png table/result_lm.csv
	Rscript -e "rmarkdown::render(\"report.Rmd\", output_format=\"html_document\")"


