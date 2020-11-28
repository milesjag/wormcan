CREATE TABLE main.electrical_activity
(
	pin_id INTEGER,
	baseline_activity: INTEGER,
	filtered_activity: INTEGER,
	is_touched: BOOLEAN,
	measured_at TIMESTAMP WITH TIME ZONE
);
