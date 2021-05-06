import typer
from api import *
from search import *
import database_service

# Add media you want blacklisted here please
MEDIA_BLACKLIST = ['t118578', 't53347', 't77063', 't95600', 't77625', 't85138', 't114044',
                   't102669', 't88061', 't107934', 't88433', 't73282', 't82322', 't95438',
                   't97924', 't97528', 't97528', 't107456', 't100085', 't103962', 't77663',
                   't97843', 't100607', 't97581', 't97716', 't85125', 't96140', 't79426',
                   't34210', 't68455', 't69180', 't77538', 't77676', 't84994', 't77675',
                   't82324', 't73287', 't80725', 't80781', 't85179', 't97767', 't97264',
                   't97920', 't77558', 't95786', 't94348', 't97797', 't97770', 't97994',
                   't97769', 't12144', 't77980', 't81044', 't80799', 't73269', 't76349',
                   't36025', 't80797', 't87987', 't113360', 't74411', 't103299', 't90166',
                   'm453831', 't97384', 't97777', 't97905', 't76291', 't73278', 't93065',
                   't73281', 't114110', 't85331', 't113208', 't124290', 't93163', 't119911',
                   't69098', 't100937', 't87597', 't78236', 't85131', 't93067', 't77719',
                   't97038', 't94341', 't84891', 't71861', 't98158', 't77535', 't122281',
                   't87642', 't88568', 't90120', 't97593', 't97597', 't97595', 't97599',
                   't97601', 't62696', 't85149', 't97377', 't97990', 't122225', 't45950',
                   't65356', 't69296', 't72504', 't72798', 't80802', 't71792', 't69342',
                   't67012', 't90215', 't36983', 't84667', 't62691', 't66328', 't66328',
                   't61460', 't77556', 't97574', 't69038', 't106918', 't76244', 't85130',
                   't42508', 't42510', 't95441', 't117990', 't98024', 't77731', 't120330',
                   't89255', 't97921', 't97673', 't98025', 't90698', 't80670', 't38441',
                   't95785', 't84820', 't114452', 't82864', 't17017', 't43295', 't98017',
                   't93861', 't97930', 't37806', 't96120', 'm47407', 't106436', 't85437',
                   't89254', 't45967', 't88042', 't77530', 't85731', 't82509', 't97772',
                   't87598', 't97792', 't112480', 't100827', 'm204450', 't99115', 't56090',
                   't85732', 'm9725', 'm11845', 't105059', 't98973', 't79641', 't97876',
                   't97578', 't97465', 't89827', 't98971', 't98159', 't85576', 't45079',
                   't95788', 't87643', 't123928', 't97397', 't42881', 't97896', 't74083',
                   't37437', 't42821', 't112485', 't22098', 't103246', 't106676', 't65676',
                   't67346', 't75992', 't62283', 't105072', 't62227', 't42671']

app = typer.Typer()


@app.command()
def update_media(total_pages: int):
    try:
        trending_media = get_all_trending_media(total_pages)

        # Fills the database with media
        database_service.dump_media_to_db(trending_media)

        # Meilisearch indexing of trending_movies
        movies_tv_index.add_documents(trending_media)
    except Exception as e:
        typer.echo('Failed to add element', e)

    remove_adult()
    typer.echo(f'Media has been updated with {total_pages} new pages')


@app.command()
def remove_adult():
    for media_id in MEDIA_BLACKLIST:
        movies_tv_index.delete_document(media_id)
    typer.echo(f'Removed {len(MEDIA_BLACKLIST)} blacklisted media elements')


if __name__ == "__main__":
    app()