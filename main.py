import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# Dicționarul cu prețurile
preturi = {
    'Tac de biliard': 2000,
    'Ciocan': 2000,
    'Cheie Franceza': 2000,
    'Rozeta': 2000,
    'Ranga metalica': 2000,
    'Bata metalica': 3000,
    'Binoclu': 3000,
    'Lanterna': 3000,
    'Cutit pumnal': 3500,
    'Briceag': 4000,
    'Maceta': 4000,
    'Baioneta': 4500,
    'Toporisca': 4500,
    'Topor de lupta': 5500,
    'cutie Tac de biliard': 10000,
    'cutie ciocan': 10000,
    'cutie cheie franceza': 10000,
    'cutie rozeta': 10000,
    'cutie ranga metalica': 10000,
    'cutie bata metalica': 15000,
     'cutie binoclu': 16000,
     'cutie lanterna': 16000,
     'cutie cutit pumnal': 15000,
     'cutie briceag': 20000,
     'cutie maceta': 20000,
     'cutie baioneta': 22500,
     'cutie toporisca': 22500,
     'cutie topor de lupta': 30000,

}

# Listă temporară pentru obiectele selectate
cos_cumparaturi = []

@bot.command(name='adauga', help='Adaugă un obiect în coșul de cumpărături. Exemplu: /adauga Tac de biliard 2')
async def adauga_in_cos(ctx, *args):
    if len(args) < 2:
        await ctx.send('Comanda incorectă. Exemplu: `/adauga Tac de biliard 2`')
        return

    obiect_input = ' '.join(args[:-1]).lower()
    cantitate = int(args[-1])

    obiect_gasit = None
    for obiect in preturi:
        if obiect_input in obiect.lower():
            obiect_gasit = obiect
            break

    if obiect_gasit:
        pret_obiect = preturi[obiect_gasit]
        cost_obiect = cantitate * pret_obiect
        cos_cumparaturi.append((obiect_gasit, cantitate, cost_obiect))
        await ctx.send(f'Ai adăugat {cantitate} bucăți de {obiect_gasit} în coș. Cost parțial: {cost_obiect}')
    else:
        await ctx.send(f'Obiectul {obiect_input} nu a fost găsit în lista de prețuri.')

@bot.command(name='comanda', help='Afișează totalul plății pentru obiectele din coș.')
async def afiseaza_cos(ctx):
    total_plata = sum(cost for _, _, cost in cos_cumparaturi)

    if cos_cumparaturi:
        for obiect, cantitate, cost in cos_cumparaturi:
            await ctx.send(f'{cantitate} bucăți de {obiect} - Cost parțial: {cost}')
        await ctx.send('████████████████████████████')
        manager_role_id = 1201689495330619413  # Replace with the actual role ID of the
        manager_role = ctx.guild.get_role(manager_role_id)

        if manager_role:
          await ctx.send(
            f'{ctx.author.mention} un {manager_role.mention} se va ocupa de comanda ta in cel mai scurt timp posibil.') 
          
          await ctx.send(f'Total de plată pentru toate obiectele: **{total_plata}** impachetați')
          cos_cumparaturi.clear()  # Curățăm lista după ce am afișat totalul

@bot.command(name='anuleaza', help='Anulează comanda curentă și golește coșul de cumpărături.')
async def anuleaza_comanda(ctx):
    cos_cumparaturi.clear()
    await ctx.send('Comanda a fost anulată și coșul de cumpărături a fost golit.')

@bot.event
async def on_ready():
    print(f'{bot.user} s-a conectat la Discord!')

bot.run('MTIwMTI5NzE1OTM4ODE1NTk1NA.GviI3r.ssWFf3Qn_bYZzsbZEbF3fSi9IC_DVlXKBV4u_k')