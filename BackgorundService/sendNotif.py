from discord_webhook import DiscordWebhook, DiscordEmbed
def send(chapter):
 
    webhook = DiscordWebhook(content="<@&595718631984332811>", url='https://discordapp.com/api/webhooks/595905581181698048/qfdi8ZyuuvokzcXThH4JC7iO6_0q4dEhU5MXaM2Yfl56nGiRYOYC66QukxB7gCykhEF6')
    webhook.execute()

    domainName = "firesyndicate.tk"
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/595905581181698048/qfdi8ZyuuvokzcXThH4JC7iO6_0q4dEhU5MXaM2Yfl56nGiRYOYC66QukxB7gCykhEF6')
    embed=DiscordEmbed(title="Chapter {num} | {name}".format(num= chapter.number, name= chapter.name) ,
    url="{domain}{chUrl}".format(domain= domainName,chUrl =chapter.get_absolute_url() ),
    description=chapter.comic.description, color=0x4ac6df)
    embed.set_author(name=chapter.comic.title)
    embed.set_thumbnail(url = domainName + chapter.comic.cover.url)
    webhook.add_embed(embed)
    webhook.execute()
