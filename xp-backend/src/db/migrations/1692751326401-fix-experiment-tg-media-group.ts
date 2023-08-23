import { MigrationInterface, QueryRunner } from "typeorm";

export class FixExperimentTgMediaGroup1692751326401 implements MigrationInterface {
    name = 'FixExperimentTgMediaGroup1692751326401'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "experiment" DROP COLUMN "tg_media_group"`);
        await queryRunner.query(`ALTER TABLE "experiment" ADD "tg_media_group" jsonb`);
        await queryRunner.query(`ALTER TABLE "subscription" DROP CONSTRAINT "FK_8c37874e2671674e05b6a7ad186"`);
        await queryRunner.query(`ALTER TABLE "subscription" DROP CONSTRAINT "FK_311b852cec90f8f0a7a78da2164"`);
        await queryRunner.query(`ALTER TABLE "subscription" ALTER COLUMN "follower_id" SET NOT NULL`);
        await queryRunner.query(`ALTER TABLE "subscription" ALTER COLUMN "followed_id" SET NOT NULL`);
        await queryRunner.query(`ALTER TABLE "subscription" ADD CONSTRAINT "FK_8c37874e2671674e05b6a7ad186" FOREIGN KEY ("follower_id") REFERENCES "user"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
        await queryRunner.query(`ALTER TABLE "subscription" ADD CONSTRAINT "FK_311b852cec90f8f0a7a78da2164" FOREIGN KEY ("followed_id") REFERENCES "user"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "subscription" DROP CONSTRAINT "FK_311b852cec90f8f0a7a78da2164"`);
        await queryRunner.query(`ALTER TABLE "subscription" DROP CONSTRAINT "FK_8c37874e2671674e05b6a7ad186"`);
        await queryRunner.query(`ALTER TABLE "subscription" ALTER COLUMN "followed_id" DROP NOT NULL`);
        await queryRunner.query(`ALTER TABLE "subscription" ALTER COLUMN "follower_id" DROP NOT NULL`);
        await queryRunner.query(`ALTER TABLE "subscription" ADD CONSTRAINT "FK_311b852cec90f8f0a7a78da2164" FOREIGN KEY ("followed_id") REFERENCES "user"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
        await queryRunner.query(`ALTER TABLE "subscription" ADD CONSTRAINT "FK_8c37874e2671674e05b6a7ad186" FOREIGN KEY ("follower_id") REFERENCES "user"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
        await queryRunner.query(`ALTER TABLE "experiment" DROP COLUMN "tg_media_group"`);
        await queryRunner.query(`ALTER TABLE "experiment" ADD "tg_media_group" jsonb array`);
    }

}
