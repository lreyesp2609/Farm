#0018_add_trigger.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_farm_budget'),  
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE FUNCTION check_total_amount_and_price()
            RETURNS TRIGGER AS $$
            BEGIN
                IF NEW.total_amount < 0 THEN
                    NEW.total_amount = ABS(NEW.total_amount);
                    RAISE NOTICE 'Negative total_amount automatically converted to positive.';
                END IF;             
                IF NEW.unit_price < 0 THEN
                    NEW.unit_price = ABS(NEW.unit_price);
                    RAISE NOTICE 'Negative unit_price automatically converted to positive.';
                END IF;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;

            CREATE TRIGGER trigger_check_total_amount
            BEFORE INSERT OR UPDATE ON app_sale
            FOR EACH ROW
            EXECUTE FUNCTION check_total_amount_and_price();
            """
        ),
    ]
